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

        cy.CreateClient("Luan Kato", "kato@gmail.com")
        cy.CreateSolicitation()
        cy.visit('/')
        cy.ClientLogout()
        cy.CreateAdmin()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('50')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click()
        cy.GoToClient("kato@gmail.com")
        cy.get(':nth-child(4) > a').click()
        cy.get('.yes')
        cy.get('.waitingForm > form > button').click()
        cy.ClientLogout()
        cy.ChangeToAdmin()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#detailed_problem_description').type('O motor está queimado')
        cy.get('#necessary_parts').type('1x Motor Elétrico Mondial |  40cm 127v 7520')
        cy.get('.works > button').click()
        cy.get('tbody > tr > :nth-child(4)').invoke('text').should('have.string', "Ordem de Serviço")
        cy.get(':nth-child(6) > a').click()
        cy.get('#detailed_problem_description').invoke('text').should('have.string', "O motor está queimado")
        cy.get('#necessary_parts').invoke('text').should('have.string', "1x Motor Elétrico Mondial |  40cm 127v 7520") 
  })
  it('Transformação para OS com sucesso pelo funcionário', () => {
    cy.exec('python manage.py migrate')
        cy.DeleteAndCreateAdm()
        cy.visit('/')
        cy.on("uncaught:exception", (e, runnable) => {
            console.log("error", e);
            console.log("runnable", runnable);
            console.log("error", e.message);
            return false;
            });

        cy.CreateClient("Luan Kato", "kato@gmail.com")
        cy.CreateSolicitation("Geladeira", "BRM56BK", "Brastemp", "Não tá gelando e ta com cheiro forte de queimado")
        cy.visit('/')
        cy.ClientLogout()
        cy.CreateAdmin()
        cy.get('.new-employee-button')
        cy.CreateEmployee()
        cy.get('.logout').click()
        cy.GoToEmployee()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('175.00')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click()
        cy.GoToClient("kato@gmail.com")
        cy.get(':nth-child(4) > a').click()
        cy.get('.waitingForm > form > button').click()
        cy.get('.logout').click()
        cy.get('#employee > a').click()
        cy.get('#email').type("robson@robson.com")
        cy.get('#password').type('ViraPag')
        cy.get('button').click()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#detailed_problem_description').type('O compressor queimou')
        cy.get('#necessary_parts').type('1x Compressor Tecumseh 1/4 HP 60Hz 110V')
        cy.get('.works > button').click()
        cy.get('tbody > tr > :nth-child(4)').invoke('text').should('have.string', "Ordem de Serviço")
        cy.get(':nth-child(6) > a').click()
        cy.get('#detailed_problem_description').invoke('text').should('have.string', "O compressor queimou")
        cy.get('#necessary_parts').invoke('text').should('have.string', "1x Compressor Tecumseh 1/4 HP 60Hz 110V")
  })
  it('Campos Vazios', () => {
    cy.exec('python manage.py migrate')
        cy.DeleteAndCreateAdm()
        cy.visit('/')
        cy.on("uncaught:exception", (e, runnable) => {
            console.log("error", e);
            console.log("runnable", runnable);
            console.log("error", e.message);
            return false;
            });

        cy.CreateClient("Luan Kato", "kato@gmail.com")
        cy.CreateSolicitation()
        cy.visit('/')
        cy.ClientLogout()
        cy.CreateAdmin()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('50')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click()
        cy.GoToClient("kato@gmail.com")
        cy.get(':nth-child(4) > a').click()
        cy.get('.yes')
        cy.get('.waitingForm > form > button').click()
        cy.ClientLogout()
        cy.ChangeToAdmin()
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('#detailed_problem_description').type(' ')
        cy.get('#necessary_parts').type(' ')
        cy.get('.works > button').click()
        cy.get('.works > :nth-child(3)').invoke('text').should("have.string", "O campo não pode ser vazio!")
        cy.get('.works > :nth-child(6)').invoke('text').should("have.string", "O campo não pode ser vazio!")
  })
})