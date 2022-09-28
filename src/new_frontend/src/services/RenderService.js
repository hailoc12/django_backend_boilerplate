import axios from 'src/utils/axios';

export const getRenderTemplates = async () => {
    const response = await axios.get('/v1/render_template/');
    return response.data;
}