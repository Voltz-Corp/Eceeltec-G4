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

  describe('home page', () => {
    // it('Definindo data com sucesso', () => {
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
    //     cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
    //     cy.get('.content > form > button').click()
    //     cy.get('.logout > button').click()
    //     cy.GoToClient()
    //     cy.get('tbody > tr > :nth-child(3)').invoke('text').should('have.string', "18 de Junho de 2024")
    //     cy.get('.AGENDADO').invoke('text').should('have.string', 'Agendado')

    //  })

    // it('Definindo orçamento com sucesso', () => {
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
    //     cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
    //     cy.get('.content > form > button').click()
    //     cy.get('#status').select('Aguardando orçamento')
    //     cy.get('.content > form > button').click()
    //     cy.get('.budgetContainer > input').type('50')
    //     cy.get('.content > form > button').click()
    //     cy.get('.logout > button').click()
    //     cy.GoToClient()
    //     cy.get(':nth-child(4) > a').click()
    //     cy.get('.price > span').invoke('text').should('have.string', "50,00")
    //     cy.get('.waitingForm > p').invoke('text').should('have.string', "Você deseja prosseguir com o serviço?")

    //  })
  
      it('inserindo data inválida', () => {
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
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2020-01-12')
        cy.get('.content > form > button').click()
        cy.get('span').invoke('text').should('have.string','A data precisa estar entre 2024-06-05 e 2024-07-05!')
       
    })
    })
