import axios from 'axios'

// Create axios instance with base configuration
const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

// API endpoints
export const endpoints = {
  facts: '/facts/',
  factAdd: '/facts/add/',
  factDetail: (id) => `/facts/${id}/`,
  categories: '/categories/',
}

export default api
