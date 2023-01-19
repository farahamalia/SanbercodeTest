/// <reference types="Cypress" />

describe("My First Test", () => {

  it('login is success', () => {
    cy.visit("https://the-internet.herokuapp.com/login")
    // Fill the username
    cy.get("#username").type("tomsmith")  
    .should("have.value","tomsmith")
    // Fill the password
    cy.get("#password").type("SuperSecretPassword!")
    .should("have.value","SuperSecretPassword!")
    // Locate and submit the form
    cy.get(".fa").click()
    
  })
  it("login is fail", () =>{
    cy.visit("https://the-internet.herokuapp.com/login")
    // Fill the username
    cy.get("#username").type("tomsmith")  
    .should("have.value","tomsmith")
    // Fill the password
    cy.get("#password").type("salah")
    //.should("have.value","SuperSecretPassword!")
    // Locate and submit the form
    cy.get(".fa").click();
    cy.get('#flash')
  }
  )

  
  
});
