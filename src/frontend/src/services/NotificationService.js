import axios from 'src/utils/axios';

export const getNotifications = async () => {
    const response = await axios.get('/v1/notification');

    return response.data;
}

