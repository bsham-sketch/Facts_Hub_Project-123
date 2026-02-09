import axios from "axios";

const api = axios.create({
  baseURL: "https://beni-backend-iuba.onrender.com",
  timeout: 10000,
});

export default api;
