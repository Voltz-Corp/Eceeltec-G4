describe('Service filtering test', () =>{
    it('successfully filtering services as employee', () => {
        cy.exec('python manage.py migrate')
        cy.DeleteAndCreateAdm()
        cy.visit('/')
        cy.on("uncaught:exception", (e, runnable) => {
            console.log("error", e);
            console.log("runnable", runnable);
            console.log("error", e.message);
            return false;
            });
        
        cy.CreateClient()
        cy.CreateSolicitation()
        cy.get('.new-request').click()
        cy.get(':nth-child(2) > :nth-child(1) > input').type('Ar condicionado')
        cy.get(':nth-child(3) > :nth-child(1) > input').type('Philco')
        cy.get(':nth-child(3) > :nth-child(2) > input').type('CL Mod 02')
        cy.get('#description').type('Está com cheiro de queimado')
        cy.get('#submit_button').click()
        cy.ClientLogout()
        cy.CreateAdmin()
        cy.CreateEmployee()
        cy.Logout()
        cy.GoToEmployee()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(1) > :nth-child(6) > a').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.scheduleDateContainer > input').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('400')
        cy.get('.content > form > button').click()
        cy.Logout()
        cy.GoToClient()
        cy.get(':nth-child(1) > :nth-child(4) > .view > button').click()
        cy.get('.waitingForm > form > button').click()
        cy.ClientLogout()
        cy.get('#employee > a').click()
        cy.get('#email').type('robson@robson.com')
        cy.get('#password').type('ViraPag')
        cy.get('button').click()
        cy.CreateOrder()
        cy.get('.openFilterModalBtn').click()
        cy.get('#orderType').select('Ordem de Serviço')
        cy.get('#orderStatus').select('Em reparo')
        cy.get('.applyFilters').click()

        cy.get('tbody > tr > :nth-child(3)').invoke('text').should('have.string', 'Ventilador | VSP40C')
        cy.get('table').contains('Ar condicionado | CL Mod 02').should('not.exist') 
        
    })

    it('successfully filtering services as admin', () => {
        cy.exec('python manage.py migrate')
        cy.DeleteAndCreateAdm()
        cy.visit('/')
        cy.on("uncaught:exception", (e, runnable) => {
            console.log("error", e);
            console.log("runnable", runnable);
            console.log("error", e.message);
            return false;
            });
        cy.CreateClient()
        cy.CreateSolicitation('Geladeira', 'Brastemp', 'BRM56BK')
        cy.get('.new-request').click()
        cy.get(':nth-child(2) > :nth-child(1) > input').type('Ar condicionado')
        cy.get(':nth-child(3) > :nth-child(1) > input').type('Philco')
        cy.get(':nth-child(3) > :nth-child(2) > input').type('CL Mod 02')
        cy.get('#description').type('Está com cheiro de queimado')
        cy.get('#submit_button').click()
        cy.ClientLogout()
        cy.CreateAdmin()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(1) > :nth-child(6) > a').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.scheduleDateContainer > input').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('400')
        cy.get('.content > form > button').click()
        cy.Logout()
        cy.GoToClient()
        cy.get(':nth-child(1) > :nth-child(4) > .view > button').click()
        cy.get('.waitingForm > form > button').click()
        cy.ClientLogout()
        cy.get('#employee > a').click()
        cy.get('#email').type('eceel-Tec@eceeltec.com')
        cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
        cy.get('button').click()
        cy.get(':nth-child(1) > a').click()
        cy.CreateOrder()
        cy.get('.openFilterModalBtn').click()
        cy.get('#orderType').select('Solicitação')
        cy.get('#orderStatus').select('Em análise')
        cy.get('.applyFilters').click()
        cy.get('tbody > tr > :nth-child(3)').invoke('text').should('have.string', 'Ar condicionado | CL Mod 02')
        })

    // it('successfully filtering services as client', () => {
    //     cy.exec('python manage.py migrate')
    //     cy.DeleteAndCreateAdm()
    //     cy.visit('/')
    //     cy.on("uncaught:exception", (e, runnable) => {
    //         console.log("error", e);
    //         console.log("runnable", runnable);
    //         console.log("error", e.message);
    //         return false;
    //         });
    // })
})