Cypress.Commands.add('deleteAndCreateAdm', () => {
  cy.exec('python test_initiate.py', { failOnNonZeroExit: false })
});

Cypress.Commands.add('createClient', ()=> {
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

Cypress.Commands.add('goToClient', () => {
  cy.get('#client > a').click()
  cy.get('#email').type('gael@gmail.com')
  cy.get('#password').type('GatoLindo')
  cy.get('button').click()
})

Cypress.Commands.add('clientLogout', () => {
  cy.visit('/');
  cy.get('#employee > a').click()
  cy.get('#logout').click()
})

Cypress.Commands.add('createAdmin', () => {
  cy.get('#employee > a').click()
  cy.get('#email').type('eceel-Tec@eceeltec.com')
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('button').click()
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('#new_password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('.form-card > form > button').click()
  cy.get('.employees > a').click()
})

Cypress.Commands.add('changeToAdmin', () => {
  cy.get('#employee > a').click()
  cy.get('#email').type('eceel-Tec@eceeltec.com')
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('button').click()
})

Cypress.Commands.add('createSolicitation', () => {
  cy.createClient()
  cy.get('.new-request').click()
  cy.get(':nth-child(2) > :nth-child(1) > input').type('Ventilador')
  cy.get(':nth-child(3) > :nth-child(1) > input').type('Mondial')
  cy.get(':nth-child(3) > :nth-child(2) > input').type('VSP40C')
  cy.get('#description').type('Está com cheiro de queimado')
  cy.get('#submit_button').click()
})

Cypress.Commands.add('createOrder', () => {
  cy.get(':nth-child(6) > a').click()
  cy.get('#detailed_problem_description').type('Tá quebrado')
  cy.get('#necessary_parts').type("Por enquanto, nenhuma")
  cy.get('.works > button').click()
})

Cypress.Commands.add('createEmployee', () => {
  cy.get('.employees > a').click()
  cy.get('.new-employee-button').click()
  cy.get('#username').type('Robson')
  cy.get('#phone').type('81900028922')
  cy.get('#email').type('robson@gmail.com')
  cy.get('#password').type('ViraPag')
  cy.get('#cep').type('31980-230')
  cy.get('#identity_number').type('861.776.720-00')
  cy.get('#position').type('funcionario')
  cy.get('#dob').invoke('removeAttr', 'type').type('2022-12-01')
  cy.get('.new-employee-button').click()
})

describe('home page', () => {
  it('Designar um técnico com sucesso', () => {
      cy.exec('python manage.py migrate')
      cy.deleteAndCreateAdm()
      cy.visit('/')
      cy.on("uncaught:exception", (e, runnable) => {
          console.log("error", e);
          console.log("runnable", runnable);
          console.log("error", e.message);
          return false;
          });

      cy.createSolicitation()
      cy.visit('/')
      cy.clientLogout()
      cy.createAdmin()
      cy.get(':nth-child(1) > a').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('#status').select('Aguardando orçamento')
      cy.get('.content > form > button').click()
      cy.get('.budgetContainer > input').type("200")
      cy.get('#status').select('Aguardando confirmação')
      cy.get('.content > form > button').click()
      cy.get('.logout > button').click()
      cy.goToClient()
      cy.get(':nth-child(4) > a').click()
      cy.get('.yes > label').click()
      cy.get('.waitingForm > form > button').click()
      cy.clientLogout()
      cy.changeToAdmin()
      cy.createEmployee()
      cy.get('#sidebarNav > ul > :nth-child(1)').click()
      cy.createOrder()
      cy.get(':nth-child(6) > a').click()
      cy.get('#tecnician').select("Robson")
      cy.get('.update').click()
      cy.get('.employee').invoke('text').should("have.string", "Robson")
   })
})