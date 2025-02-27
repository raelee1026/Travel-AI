import React, { useEffect } from 'react'
// import { GooglePlacesAutocomplete } from 'react-native-google-places-autocomplete'
import { useState } from 'react'
import {Input} from '@/components/ui/input'
import { SelectBudgetOptions, SelectTravelesList } from '@/constants/options';
import { Button } from '@/components/ui/button';
import { Link, useNavigate } from 'react-router-dom';
import GooglePlacesAutocomplete from "react-google-places-autocomplete";

function CreateTrip() {
    const navigate = useNavigate();
    const [place, setPlace] = useState();

    const [formData, setFormData] = useState([]);

    const handleInputChange = (name, value)=>{

        setFormData({
            ...formData,
            [name]: value
        })
    }

    useEffect(() => {
        console.log(formData);
    }, [formData])

    const OnGenerateTrip=()=>{
        if(formData?.noOfDays<1){
            alert('Please enter valid number of days')
            return;
        }
        if(!formData?.destination || !formData?.noOfDays || !formData?.travelDate || !formData?.budget || !formData?.traveler || !formData?.info){
            alert('Please fill all the fields') 
            return;
        }
        console.log(formData); 

        const prompt = `
        You are an expert travel agent AI. Plan a trip with the following details:

        Destination: ${formData.destination}
        Number of Days: ${formData.noOfDays}
        Travel Date: ${formData.travelDate}
        Budget: ${formData.budget}
        Number of Travelers: ${formData.traveler}
        Additional Information: ${formData.info}

        Please provide a detailed itinerary, including daily activities, accommodations, and travel tips.
    `;

    console.log(prompt);
    // sent the prompt to the chat page
    navigate('/chat', { state: { initialPrompt: prompt } });
    };

  return (
    <div className='sm:px-10 md:px-32 lg:px-56 xl:px-10 px-5 mt-10'>
        <h2 className='font-bold text-3xl'>Tell us your travel preferences</h2>
        <p className='mt-3 text-gray-500 text-xl'>Just provide some basic information, and our trip planner will generate a customized itinerary based on your preferences.</p>

        <div className='mt-20 flex flex-col gap-10'>
            <div>
                <h2 className='text-xl my-3 font-medium'>What is destination of choice?</h2>
                {/* <GooglePlacesAutocomplete apiKey={import.meta.env.VITE_GOOGLE_PLACE_API_KEY}></GooglePlacesAutocomplete> */}
                {/* <GooglePlacesAutocomplete
                    apiKey={import.meta.env.VITE_GOOGLE_PLACE_API_KEY}
                    selectProps={{
                    onChange: (place) => console.log(place),
                    }}
                /> */}
                <Input placeholder={'Ex:Taiwan'} type="default" onChange={(e)=>handleInputChange('destination', e.target.value)}></Input>
            </div>

            <div>
                <h2 className='text-xl my-3 font-medium'>When are you leaving?</h2>
                <Input type="date" onChange={(e)=>handleInputChange('travelDate', e.target.value)}></Input>
            </div>

            <div>
                <h2 className='text-xl my-3 font-medium'>How many days?</h2>
                <Input placeholder={'Ex:3'} type="number" onChange={(e)=>handleInputChange('noOfDays', e.target.value)}></Input>
            </div>


            <div>
                <h2 className='text-xl my-3 font-medium'>What is your budget?</h2>
                <div className='grid grid-cols-3 gap-5 mt-5'>
                    {SelectBudgetOptions.map((item, index) => (
                        <div key={index} 
                        onClick={()=>handleInputChange('budget', item.title)}
                        className={`p-4 border rounded-lg hover:shadow-lg cursor-pointer ${
                            formData?.budget === item.title ? 'shadow-lg border-black' : ''
                        }`}>
                            <h2 className='text-4xl'>{item.icon}</h2>
                            <h2 className='font-bold text-lg'>{item.title}</h2>
                            <h2 className='text-sm text-gray-500'>{item.desc}</h2>
                        </div>
                        ))}
                </div>

            </div>

            <div>
                <h2 className='text-xl my-3 font-medium'>Who do you plan traveling with?</h2>
                <div className='grid grid-cols-2 gap-5 mt-5'>
                    {SelectTravelesList.map((item, index) => (
                        <div key={index} 
                        onClick={()=>handleInputChange('traveler', item.people)}
                        className={`p-4 border rounded-lg hover:shadow-lg cursor-pointer ${
                            formData?.traveler === item.people ? 'shadow-lg border-black' : ''
                        }`}>
                            <h2 className='text-4xl'>{item.icon}</h2>
                            <h2 className='font-bold text-lg'>{item.title}</h2>
                            <h2 className='text-sm text-gray-500'>{item.desc}</h2>
                        </div>
                        ))}
                </div>

            </div>

            <div>
                <h2 className='text-xl my-3 font-medium'>Any more Information?(necessary)</h2>
                <Input placeholder={'Ex: one of us is vegetarian'} type="default" onChange={(e)=>handleInputChange('info', e.target.value)}></Input>
            </div>

        </div>

        <div className='my-10 justify-end flex'>
            <Button onClick={OnGenerateTrip}>Generate Trip</Button>
        </div>

        

    </div>
  )
}

export default CreateTrip