import axios from "axios";

const api = axios.create({
  baseURL: "https://beni-backend-iuba.onrender.com",
});

export default api;