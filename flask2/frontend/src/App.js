import { React } from 'react'
import { HashRouter, Routes, Route } from "react-router-dom"
import Users from './component/Users'
import About from './component/About'
import Layout from './component/Layout'

function App() {
  return (
    <HashRouter>
      <Layout>
        <Routes>
          <Route path="/" element={<Users />} />
          <Route path="/about" element={<About />} />
          <Route path="/users" element={<Users />} />
        </Routes>
      </Layout>
    </HashRouter>
  )
}

export default App