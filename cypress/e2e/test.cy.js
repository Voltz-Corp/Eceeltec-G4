
Cypress.Commands.add('DeleteAndCreateAdm', () => {
  cy.exec('python test_initiate.py', { failOnNonZeroExit: false })
});

Cypress.Commands.add('CreateClient', ()=> {
  cy.get('#client > a').click()
  cy.get('a').click()
  cy.get('#toggleAddress').click()
  cy.get('#name').type('Gabriel Albuquerque')
  cy.get('#phone').type('81900028922')
  cy.get('#email').type('gael@gmail.com')
  cy.get('#password').type('GatoLindo')
  cy.get('#cep').type('31980-230')
  cy.get('#number').type('356')
  cy.get('button').click()
  cy.get('#email').type('gael@gmail.com')
  cy.get('#password').type('GatoLindo')
  cy.get('button').click()
})

Cypress.Commands.add('ClientLogout', () => {
  cy.visit('/');
  cy.get('#employee > a').click()
  cy.get('#logout').click()
})

Cypress.Commands.add('CreateEmployee', () => {

})
describe('home page', () => {
  it('passes', () => {
    cy.exec('python manage.py migrate')
    cy.DeleteAndCreateAdm()

    cy.visit('/');
    
    //menuHamburger not defined!?
    cy.on("uncaught:exception", (e, runnable) => {
      console.log("error", e);
      console.log("runnable", runnable);
      console.log("error", e.message);
      return false;
      });

      // cy.get('#employee > a').click()
      // cy.get('#email').type('eceel-Tec@eceeltec.com')
      // cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
      // cy.get('button').click()

      // cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
      // cy.get('#new_password').type('obGWjpaTayKJWpBiFSMm')
      // cy.get('.form-card > form > button').click()
      // cy.get('.employees > a').click()
      // cy.get('.new-employee-button').click()
      // cy.get('#username').type('Gabriel Albuquerque')
      // cy.get('#phone').type('81900028922')
      // cy.get('#email').type('gael@gmail.com')
      // cy.get('#password').type('GatoLindo')
      // cy.get('#cep').type('31980-230')
      // cy.get('#identity_number').type('861.776.720-00')
      // cy.get('#position').type('funcionario')
      // cy.get('#dob').click()
      // cy.get('#dob').type('11')
          })
})
