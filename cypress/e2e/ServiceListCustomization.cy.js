describe('Service filtering test', () =>{
    it('successfully filtering services as client', () => {
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
        cy.Logout()
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
    })

    // it('successfully filtering services as admin', () => {
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

    // it('successfully filtering services as employee', () => {
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