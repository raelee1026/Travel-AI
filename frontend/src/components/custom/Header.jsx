import React from 'react'
import { Button } from '@/components/ui/button'

function Header() {
  return (
    <div className='p-3 shadow-sm flex justify-between items-center px-5'>
        <img src='/travel.svg' className='w-16 h-16'></img>
        <img src='/travel.svg' className='w-16 h-16'></img>
        {/* <div>
            <Button>Sign In</Button>
        </div> */}
    </div>
  )
}

export default Header