Cypress.Commands.add('DeleteAndCreateAdm', () => {
  cy.exec('python test_initiate.py', { failOnNonZeroExit: false })
});

Cypress.Commands.add('CreateClient', (name = "Gabriel Albuquerque", email = "teste@teste.com") => {
  cy.get('#client > a').click()
  cy.get('a').click()
  cy.get('#toggleAddress').click()
  cy.get('#name').type(name)
  cy.get('#phone').type('81900028922')
  cy.get('#email').type(email)
  cy.get('#password').type('GatoLindo')
  cy.get('#cep').type('31980-230')
  cy.get('#number').type('356')
  cy.get('button').click()
  cy.get('#email').type(email)
  cy.get('#password').type('GatoLindo')
  cy.get('button').click()
})

Cypress.Commands.add('CreateOrder', () => {
  cy.get(':nth-child(6) > a').click()
  cy.get('#detailed_problem_description').type('Cabos corroídos')
  cy.get('#necessary_parts').type("5 cabos")
  cy.get('.works > button').click()
})

Cypress.Commands.add('CreateEmployee', (name = "Robson", email = "robson@robson.com") => {
  cy.get('.new-employee-button').click()
  cy.get('#username').type(name)
  cy.get('#phone').type('81900028922')
  cy.get('#email').type(email)
  cy.get('#password').type('ViraPag')
  cy.get('#cep').type('31980-230')
  cy.get('#identity_number').type('861.776.720-00')
  cy.get('#position').type('funcionario')
  cy.get('#dob').invoke('removeAttr', 'type').type('2022-12-01')
  cy.get('.new-employee-button').click()
})

Cypress.Commands.add('CreateSolicitation', () => {
  cy.get('.new-request').click()
  cy.get(':nth-child(2) > :nth-child(1) > input').type('Ventilador')
  cy.get(':nth-child(3) > :nth-child(1) > input').type('Mondial')
  cy.get(':nth-child(3) > :nth-child(2) > input').type('VSP40C')
  cy.get('#description').type('Está com cheiro de queimado')
  cy.get('#submit_button').click()
})

Cypress.Commands.add('ClientLogout', () => {
  cy.visit('/');
  cy.get('#employee > a').click()
  cy.get('#logout').click()
})

Cypress.Commands.add('GoToClient', (email = "teste@teste.com", password = "GatoLindo") => {
  cy.get('#client > a').click()
  cy.get('#email').type(email)
  cy.get('#password').type(password)
  cy.get('button').click()
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