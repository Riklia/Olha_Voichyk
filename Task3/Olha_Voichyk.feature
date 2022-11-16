Feature: testing EPAM site

  Scenario: select a language
     Given we are at "https://www.epam.com/"
      When we click on "Global (EN)" 
      Then we get a list of avaliable languages

  Scenario: send question with the empty required fields
     Given we are at "https://www.epam.com/about/who-we-are/contact"
      When we leave required fields (with *) empty
      Then we get these fields red and with the corresponding message

  Scenario: the search box works
     Given we are at "https://www.epam.com/" and click on the magnifier icon
      When we enter "Cloud" and click on the "Find"
      Then we are redirected on the results page

  Scenario: the HOW WE DO IT button works
     Given we are at "https://www.epam.com/"
      When we click on "HOW WE DO IT"
      Then we get "https://www.epam.com/how-we-do-it" opened

  Scenario: location filter works
     Given we are at "https://www.epam.com/careers"
      When we choose location Kyiv and click on "Find"
      Then we get list of job offers in Kyiv

  Scenario: return to the home page easily 
     Given we are at "https://www.epam.com/careers/job-listings?country=Ukraine&city=Kyiv"
      When we click on the "Home" label or "<epam>" icon
      Then we are redirected to "https://www.epam.com/"

  Scenario: link to EPAM LinkedIn profile works 
     Given we are at "https://www.epam.com/"
      When we click on the LinkedIn icon
      Then we have EPAM profile on LinkedIn

  Scenario: send phone number to our phone 
     Given we are at "https://www.epam.com/about/who-we-are/contact"
      When we click on "+1-267-759-9000"
      Then we are asked to choose the device to send the phone number

  Scenario: playing videos
     Given we are at "https://www.epam.com/services/consult-and-design"
      When we click on the play button
      Then the video is playing
