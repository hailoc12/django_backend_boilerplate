import axios from 'axios';

// ----------------------------------------------------------------------

const axiosInstance = axios.create({ baseURL: process.env.BACKEND_URL || 'https://api.veminhhoa.com' });

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject((error.response && error.response.data) || {message: 'Something went wrong'})
);

export default axiosInstance;
