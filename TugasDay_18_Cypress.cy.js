/// <reference types="Cypress" />

/// <reference types='Cypress' />

describe('My First Test', () => {

  it('login is success', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
    // Fill the username
    cy.get('#username')
    .type('tomsmith')  
    .should('have.value','tomsmith')
    cy.wait(3)
    // Fill the password
    cy.get('#password')
    .type('SuperSecretPassword!')
    .should('have.value','SuperSecretPassword!')
    //submit the form
    cy.get('#login').click()

  })
  it('login is fail', () =>{
    cy.visit('https://the-internet.herokuapp.com/login')
    // Fill the username
    cy.get('#username').type('tomsmith')  
    .should('have.value','tomsmith')
    cy.wait(3)
    // Fill the password
    cy.get('#password').type('salah')
    //submit the form
    cy.get('#login').click()
    cy.get('#flash-messages')
 }
)

  
  
});
