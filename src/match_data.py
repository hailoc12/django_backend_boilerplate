from embedbase_client import EmbedbaseClient
import pandas as pd
import time

# INIT


def train_data(dataset_path, database_name, embedbase, train=False):
    """Train data from dataset_path and add to database_name in embedbase"""
    """
    @Args:
        database_name: name of database in embedbase
        dataset_path: path to dataset
        embedbase: embedbase client
        train: True if you want to train, False if you want to add to database
    @Returns:
        cdt_dict: dictionary of cdt
    """

    # train dataset 1
    pd1 = pd.read_excel(dataset_path)

    # loop through pd1
    train_list = []
    cdt_dict = {}

    number = -1
    count = 0
    print("Reading data to train")

    for index, row in pd1.iterrows():
        item = {
                "ID": str(row[0]).strip() if str(row[0]).strip() != "nan" else "",
                "name": str(row[1]).strip() if str(row[1]).strip() != "nan" else "",
                "address1": str(row[2]).strip() if str(row[2]).strip() != "nan" else "",
                "address2": str(row[3]).strip() if str(row[3]).strip() != "nan" else "",
                "father_org": str(row[4]).strip() if str(row[4]).strip() != "nan" else ""
            }

        train_item = {
            "data": item["name"] + ". " + item["address1"] + ". " + item["address2"],
            "metadata": item
        }

        train_list.append(train_item)
        cdt_dict[item["ID"]] = item

        count += 1
        if number > 0 and (count >= number):
            break


    # add to embedbase

    if train:
        print("Train data")
        count = 0
        items = []
        for item in train_list:
            print("Training item: ", item["metadata"]["ID"])
            print(item)
            items.append(item)
            count += 1

            # data = embedbase.dataset(database_name).add(item["data"], metadata = item["metadata"])
            if count % 10 == 0:
                #data = embedbase.dataset(database_name).batch_add((item['data'], item['metadata'])  for item in items)
                retry = 0
                while retry < 3:
                    try:
                        data = embedbase.dataset(database_name).batch_add(items)
                        break
                    except:
                        retry += 1
                        time.sleep(5)

                print(data)
                time.sleep(0.05)
                count = 0
                items = []

        if count > 0:
            embedbase.dataset(database_name).batch_add(items)

    return cdt_dict


def match_data(dataset_path, output_path, database_name, embedbase, cdt_dict, exact_threshold=0.8, suggest_threshold=0.6, use_ss=False):
    """Search data from dataset_path and add to database_name in embedbase"""
    """
    @Args:
        database_name: name of database in embedbase
        dataset_path: path to dataset
        embedbase: embedbase client
    @Returns:
        final_dict: dictionary of cdt
    """

    # loop through pd2
    # for each row in pd2, predict the label
    pd2 = pd.read_excel(dataset_path)

    number = -1
    count = 0
    output_list = []

    for index, row in pd2.iterrows():
        item = {
                "id": str(row[0]).strip(),
                "Mã cơ quan msc cũ": str(row[1]).strip() if str(row[1]).strip() != "nan" else "",
                "mã cơ quan msc mới": str(row[2]).strip() if str(row[2]).strip() != "nan" else "",
                "Tên bên mời thầu": str(row[3]).strip() if str(row[3]).strip() != "nan" else "",
                "Địa chỉ": str(row[4]).strip() if str(row[4]).strip() != "nan" else "",
                "Cơ quan chủ quản": str(row[5]).strip() if str(row[5]).strip() != "nan" else "",
                "Match": str(row[6]).strip() if str(row[6]).strip() != "nan" else "",
                "Match Method": str(row[7]).strip() if str(row[7]).strip() != "nan" else ""
            }

        if item["Match"] == "" or item["Match"] == "nan":
            print()
            print("Check item: ", item["id"])
            print("Item name: ", item["Tên bên mời thầu"])
            matched = False

            if item["mã cơ quan msc mới"] in cdt_dict:
                print("Found item by ID: ", item["mã cơ quan msc mới"])
                origin_item= cdt_dict[item["mã cơ quan msc mới"]]
                item["Cơ quan chủ quản"] = origin_item["father_org"]
                item["Match"] = origin_item["name"]
                item["Match Method"] = "ID"
            else:
                if use_ss:
                    # query = item["Tên bên mời thầu"] + ". " + item["Địa chỉ"]
                    query = item["Tên bên mời thầu"] + ". " + item["Tên bên mời thầu"] + ". " + item["Địa chỉ"]
                    retry = 0
                    data = None
                    while retry < 3:
                        try:
                            data = embedbase.dataset(database_name).search(query, limit=1).get()
                            break
                        except:
                            retry += 1
                            time.sleep(5)

                    # check exact match
                    result = [x for x in data if x.similarity > exact_threshold]
                    if result:
                        origin_item = result[0].metadata
                        print("Found item by SS: ", origin_item)
                        print("Similarity: ", result[0].similarity)
                        item["Cơ quan chủ quản"] = origin_item["father_org"]
                        item["Match"] = origin_item["name"]
                        item["Match Method"] = "Similarity"
                        matched = True
                    else:
                        # check suggest match
                        result = [x for x in data if x.similarity > suggest_threshold]
                        if result:
                            origin_item = result[0].metadata
                            print("Found item by SS: ", origin_item)
                            print("Similarity: ", result[0].similarity)
                            item["Match"] = origin_item["name"]
                            item["Match Method"] = "Suggest"

            if matched:
                print("Matched item: ", item)
            #print()

        output_list.append(item)

        count +=1
        if number > 0 and count >= number:
            break

    # write to output file
    pd.DataFrame(output_list).to_excel(output_path, index=False)


def main():
    dataset1_path = "../dataset/CDT_dataset_1.xlsx"
    dataset2_path = "../dataset/CDT_dataset_2.xlsx"
    dataset3_path = "../dataset/CDT_dataset_3.xlsx"

    embedbase_url = "http://localhost:8000"
    embedbase = EmbedbaseClient(embedbase_url)
    database_name = "CDT_database_final_3"

    # cdt_dict = train_data(dataset1_path, database_name, embedbase, train=True)
    cdt_dict = train_data(dataset1_path, database_name, embedbase, train=False)
    match_data(dataset2_path, dataset3_path, database_name, embedbase, cdt_dict, exact_threshold=0.95, suggest_threshold=0.65, use_ss=True)


if __name__ == "__main__":
    main()


