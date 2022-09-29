import axios from 'src/utils/axios';

export const getPocket = async () => {
    const response = await axios.get('/v1/pocket');
    return response.data;
}