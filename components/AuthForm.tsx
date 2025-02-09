'use client';

import Link from 'next/link'
import React, { useState } from 'react'
import Image from "next/image"


import { number, z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
 

const formSchema = z.object({
	username: z.string().min(10, {
	  message: "Username must be at least 10 digits.",
	}),
	password:z.string().min(8,{
		message: "Passord must be of 8 characters"}),
	
  })



const AuthForm = ({type}:{type: string}) => {
	const [user, setuser] = useState(null);
	// 1. Define your form.
	const form = useForm<z.infer<typeof formSchema>>({
		resolver: zodResolver(formSchema),
		defaultValues: {
		  username: "",
		},
	  })
	 
	  // 2. Define a submit handler.
	  function onSubmit(values: z.infer<typeof formSchema>) {
		// Do something with the form values.
		// ✅ This will be type-safe and validated.
		console.log(values)
	  }

  return (
	<section className = "auth-form">
		<header className = 'flex flex-co gap-5 md:gap-8'>
		<Link href ="/"  className="cursor-pointer flex items-center gap-2">

			<Image 
				src ="/icons/logo.svg"
				width ={44}
				height={44}
				alt ="Smart Bank logo"
				/>
				<h1 className='text-26 font-ibm-plex-serif font-bold text-black-1'>
				Smart Banking</h1>
		</Link>	
	
		</header>

<div className = "flex flex-col gap-1 md:gap-3">
	<h1 className = "text-24 lg:text-30 font-semibold text-gray-900">
		{user 
		? 'Link Account':type ==='sign-in'?
		'Sign In':
		'Sign-Up'
		}
		<p className = "text-16 front-normal text-gray-600">

			{user
			? 'Link your Account to get Started':
			'Please enter your login details'
			}
		</p>

	</h1>
</div>

		
		{user?(
		<div className= "flex flex-col gap-4">
			{/*PlaidLink*/}

		</div>
	):(
		<>
		<Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            
             <div>
				<FormLabel
				className = "form-label">Login ID</FormLabel>

				<FormLabel>
					<div className = "flex w-full flex-col">
						<FormControl>
							<Input
							placeholder = "Enter your phone number"
							className = "input-class"
							{...field}
							/>
						</FormControl>
						<FormMessage className = "form-message mt-2"/>
					</div>
				</FormLabel>
			 </div>

          )}
        />

<FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            
             <div>
				<FormLabel
				className = "form-label">Password</FormLabel>

				<FormLabel>
					<div className = "flex w-full flex-col">
						<FormControl>
							<Input
							placeholder = "Enter your password"
							className = "input-class"
							type = "password"
							{...field}
							/>
						</FormControl>
						<FormMessage className = "form-message mt-2"/>
					</div>
				</FormLabel>
			 </div>

          )}
        />


        <Button type="submit"
		className = "form-btn">Submit</Button>
      </form>
    </Form>
		</>
	)
	}

	</section>
  )
}

export default AuthForm