import React from 'react'
import styled from 'styled-components'
// import Navbar from '../components/Navbar'
// import Button from '../components/Button'
import Vid from '../components/video'

const loginPage = () => {
  return (
    <div>
        <Section>
            {/* <Navbar/> */}
            <Vid/>
        </Section> 
    </div>
  )
}

export default loginPage

const Section = styled.nav`
    background-color: #232835;


`