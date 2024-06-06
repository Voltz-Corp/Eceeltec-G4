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

Cypress.Commands.add('GoToClient', () => {
  cy.get('#client > a').click()
  cy.get('#email').type('gael@gmail.com')
  cy.get('#password').type('GatoLindo')
  cy.get('button').click()
})

Cypress.Commands.add('ClientLogout', () => {
  cy.visit('/');
  cy.get('#employee > a').click()
  cy.get('#logout').click()
})

Cypress.Commands.add('CreateAdmin', () => {
  cy.get('#employee > a').click()
  cy.get('#email').type('eceel-Tec@eceeltec.com')
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('button').click()
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('#new_password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('.form-card > form > button').click()
  cy.get('.employees > a').click()
})

Cypress.Commands.add('ChangeToAdmin', () => {
  cy.get('#employee > a').click()
  cy.get('#email').type('eceel-Tec@eceeltec.com')
  cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
  cy.get('button').click()
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

Cypress.Commands.add('CreateOrder', () => {
  cy.get(':nth-child(6) > a').click()
  cy.get('#detailed_problem_description').type('Tá quebrado')
  cy.get('#necessary_parts').type("Por enquanto, nenhuma")
  cy.get('.works > button').click()
})

Cypress.Commands.add('CreateEmployee', () => {
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

describe('HomePage', () => {
  // it('Designar um técnico com sucesso', () => {
  //     cy.exec('python manage.py migrate')
  //     cy.DeleteAndCreateAdm()
  //     cy.visit('/')
  //     cy.on("uncaught:exception", (e, runnable) => {
  //         console.log("error", e);
  //         console.log("runnable", runnable);
  //         console.log("error", e.message);
  //         return false;
  //         });

  //     cy.CreateSolicitation()
  //     cy.visit('/')
  //     cy.ClientLogout()
  //     cy.CreateAdmin()
  //     cy.get(':nth-child(1) > a').click()
  //     cy.get(':nth-child(6) > a').click()
  //     cy.get('#status').select('Aguardando orçamento')
  //     cy.get('.content > form > button').click()
  //     cy.get('.budgetContainer > input').type("200")
  //     cy.get('.content > form > button').click()
  //     cy.get('.logout > button').click()
  //     cy.GoToClient()
  //     cy.get(':nth-child(4) > a').click()
  //     cy.get('.yes > label').click()
  //     cy.get('.waitingForm > form > button').click()
  //     cy.ClientLogout()
  //     cy.ChangeToAdmin()
  //     cy.CreateEmployee()
  //     cy.get('#sidebarNav > ul > :nth-child(1)').click()
  //     cy.CreateOrder()
  //     cy.get(':nth-child(6) > a').click()
  //     cy.get('#tecnician').select("Robson")
  //     cy.get('.update').click()
  //     cy.get('.employee').invoke('text').should("have.string", "Robson")
  //  })

   it('Remover uma ordem de serviço com sucesso', () => {
    cy.exec('python manage.py migrate')
    cy.DeleteAndCreateAdm()
    cy.visit('/')
    cy.on("uncaught:exception", (e, runnable) => {
        console.log("error", e);
        console.log("runnable", runnable);
        console.log("error", e.message);
        return false;
        });

    cy.CreateSolicitation()
    cy.visit('/')
    cy.ClientLogout()
    cy.CreateAdmin()
    cy.get(':nth-child(1) > a').click()
    cy.get(':nth-child(6) > a').click()
    cy.get('#status').select('Aguardando orçamento')
    cy.get('.content > form > button').click()
    cy.get('.budgetContainer > input').type("200")
    cy.get('.content > form > button').click()
    cy.get('.logout > button').click()
    cy.GoToClient()
    cy.get(':nth-child(4) > a').click()
    cy.get('.yes > label').click()
    cy.get('.waitingForm > form > button').click()
    cy.ClientLogout()
    cy.ChangeToAdmin()
    cy.get('ul > :nth-child(1) > a').click()
    cy.CreateOrder()
    cy.get(':nth-child(6) > a').click()
    cy.get('#status').select('Cancelado')
    cy.get('.update').click()
    cy.get('ul > :nth-child(1) > a').click()
    cy.get('.deleteOrderRequest').click()
    cy.get('.deleteRequestOrder').click()
    cy.get('tbody > tr:first-child').should("not.exist")
 })
})