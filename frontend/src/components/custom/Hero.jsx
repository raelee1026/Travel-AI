import React from 'react'
import {Button} from '@/components/ui/button'
import {Link} from 'react-router-dom'

function Hero() {
  return (
    <div className='flex flex-col items-center mx-56 gap-9'>
        <h1 className='font-extrabold text-[50px] text-center mt-16'>
            <span className='text-[#0000ff]'>Travel AI: </span><br />Personalized Itineraries
        </h1>
        <p className='text-xl test-gray-500 text-center'>Your personal trip planner and travel curator, creating custom itineraries tailored to your interests and budget.</p>
        <Link to='/create-trip'>
            <Button>Get Started</Button>
        </Link>

        {/* <Link to='/chat'>
            <Button>Chat with your AI assistant, customic for travel</Button>
        </Link> */}
        
    </div>
  )
}

export default Hero