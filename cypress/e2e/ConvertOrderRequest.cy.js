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
    
  })
  it('Campos Vazios', () => {
    
  })
})