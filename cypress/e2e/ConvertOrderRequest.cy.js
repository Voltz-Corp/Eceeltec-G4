Cypress.Commands.add('DeleteAndCreateAdm', () => {
    cy.exec('python test_initiate.py', { failOnNonZeroExit: false })
  });
  
Cypress.Commands.add('CreateClient', ()=> {
    cy.get('#client > a').click()
    cy.get('a').click()
    cy.get('#toggleAddress').click()
    cy.get('#name').type('Luan Kato')
    cy.get('#phone').type('81991899586')
    cy.get('#email').type('kato@gmail.com')
    cy.get('#password').type('GatoLindo')
    cy.get('#cep').type('31980-230')
    cy.get('#number').type('356')
    cy.get('button').click()
    cy.get('#email').type('kato@gmail.com')
    cy.get('#password').type('GatoLindo')
    cy.get('button').click()
  })

Cypress.Commands.add('GoToClient', () => {
    cy.get('#client > a').click()
    cy.get('#email').type('kato@gmail.com')
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

Cypress.Commands.add('changeToAdmin', () => {
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

describe('HomePage', () => {
  it('Transformação para OS com sucesso pelo administrador', () => {
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
        cy.get('#status').select('Aceito')

        
  })
  it('Transformação para OS com sucesso pelo funcionário', () => {
    
  })
  it('Campos Vazios', () => {
    
  })
})