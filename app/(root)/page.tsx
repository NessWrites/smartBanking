
/* eslint-disable */
import HeaderBox from '@/components/HeaderBox'
import TotalBalanceBox from '@/components/TotalBalanceBox';
import RightSidebar from '@/components/ui/RightSidebar';
import React from 'react'
import Image from "next/image";

const Home = () => {
	const loggedIn = {firstName: 'Ness', lastName:'Stha',
		email: 'ness_stha@gmail.com'
	};
  return (
	<section className='home'>
<div className='home-content'>

<header className='home-header'>
	<HeaderBox
	type = "greeting"
	title = "Welcome"
	user ={loggedIn?.firstName|| 'Guest'}
	subtext = "Access and manage your account and transactions efficiently."
	
	/>

	<TotalBalanceBox
	accounts ={[]}
	totalBanks ={1}
	totalCurrentBalance ={1250.35}
	/>
</header>
RECENT TRANSACTIONS
</div>

<RightSidebar
user = {loggedIn}
transactions = {[]}
banks = {[{currentBalance:1234.50},
{currentBalance:2234.50}]}
/>
	</section>
  )
}

export default Home