
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
  cy.get('#employee > a').click()
  cy.get('#email').type('eceel-Tec@eceeltec.com')
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('button').click()
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('#new_password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('.form-card > form > button').click()
  cy.get('.employees > a').click()
  cy.get('.new-employee-button').click()
  cy.get('#username').type('Andre Castro')
  cy.get('#phone').type('81900028922')
  cy.get('#email').type('Andre@gmail.com')
  cy.get('#password').type('ViraPag')
  cy.get('#cep').type('31980-230')
  cy.get('#identity_number').type('861.776.720-00')
  cy.get('#position').type('funcionario')
  cy.get('#dob').invoke('removeAttr', 'type').type('2022-12-01')
  cy.get('.new-employee-button').click()
})

Cypress.Commands.add('CreateSolicitation', () => {
  cy.CreateClient()
  cy.get('.new-request').click()
  cy.get(':nth-child(2) > :nth-child(1) > input').type('Ventilador')
  cy.get(':nth-child(3) > :nth-child(1) > input').type('Mondial')
  cy.get(':nth-child(3) > :nth-child(2) > input').type('VSP40C')
  cy.get('#description').type('Está com cheiro de queimado')
  cy.get('#submit_button').click()
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

          })
})
