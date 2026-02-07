import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import Categories from './pages/Categories'
import FactsList from './pages/FactsList'
import FactDetails from './pages/FactDetails'
import AddFact from './pages/AddFact'
import About from './pages/About'
import Blog from './pages/Blog'
import BlogPost from './pages/BlogPost'

function App() {
  return (
    <div className="app-container">
      <Navbar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/categories" element={<Categories />} />
          <Route path="/facts" element={<FactsList />} />
          <Route path="/facts/category/:category" element={<FactsList />} />
          <Route path="/fact/:id" element={<FactDetails />} />
          <Route path="/add-fact" element={<AddFact />} />
          <Route path="/about" element={<About />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/blog/:id" element={<BlogPost />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}

export default App