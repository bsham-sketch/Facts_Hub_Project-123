import React from 'react'
import { Link } from 'react-router-dom'

const Blog = () => {
  const blogPosts = [
    {
      id: 1,
      title: "The Science Behind Everyday Phenomena",
      excerpt: "Discover the fascinating science that explains common occurrences in our daily lives.",
      date: "January 15, 2024",
      category: "Science"
    },
    {
      id: 2,
      title: "How Technology is Shaping Our Future",
      excerpt: "Explore the latest technological advancements and their potential impact on society.",
      date: "January 10, 2024",
      category: "Technology"
    },
    {
      id: 3,
      title: "The Health Benefits of Common Foods",
      excerpt: "Learn about the nutritional value and health benefits of foods you eat every day.",
      date: "January 5, 2024",
      category: "Health"
    }
  ]

  return (
    <div className="max-w-4xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">Facts Hub Blog</h1>
        <p className="text-xl text-gray-600">
          Insights, discoveries, and interesting reads about the world around us.
        </p>
      </div>

      <div className="space-y-8">
        {blogPosts.map(post => (
          <article key={post.id} className="bg-white rounded-lg shadow-md p-8">
            <div className="flex justify-between items-start mb-4">
              <div>
                <span className="category-badge">{post.category}</span>
                <h2 className="text-2xl font-bold text-gray-900 mt-2 mb-2">{post.title}</h2>
                <p className="text-gray-600">{post.date}</p>
              </div>
            </div>
            <p className="text-gray-700 mb-6 leading-relaxed">
              {post.excerpt}
            </p>
            <div className="flex justify-between items-center">
              <div className="text-sm text-gray-500">
                Read time: 3-5 minutes
              </div>
              <Link 
                to={`/blog/${post.id}`}
                className="btn-secondary"
              >
                Read More
              </Link>
            </div>
          </article>
        ))}
      </div>

      <div className="mt-12 text-center">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">Stay Updated</h2>
        <p className="text-gray-600 mb-6">
          New blog posts are added regularly. Check back often for more interesting content!
        </p>
        <div className="space-x-4">
          <Link to="/categories" className="btn-primary">
            Explore Facts
          </Link>
          <Link to="/add-fact" className="btn-secondary">
            Share Your Knowledge
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Blog