import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import CreateTrip from './create-trip/index.jsx'
import Chat from './chat/index.jsx'
import Header from './components/custom/Header.jsx'

const router = createBrowserRouter([
  {
    path:'/', 
    element: <App/>
  },
  {
    path:'/create-trip',
    element: <CreateTrip/>
  },
  {
    path:'/chat',
    element: <Chat/>
  }
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Header/>
    <RouterProvider router={router} />
  </StrictMode>,
)
