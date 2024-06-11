describe('Reopening Service Tests', () => {
  it('Reopening with sucess', () => {

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
      cy.visit('/')
      cy.ClientLogout()
      cy.CreateAdmin()

      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
      cy.get('.content > form > button').click()
      cy.get('.content > form > button').click()
      
      cy.get('.budgetContainer > input').type('90')
      cy.get('.content > form > button').click()
      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('.waitingForm > form > button').click()
      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.works > button').click()

      cy.get('#detailed_problem_description').type('Muito pelo de gato dentro do motor está interferindo na ventilação interna')
      cy.get('#necessary_parts').type('Nenhuma, apenas limpeza')
      cy.get('.works > button').click()

      cy.get(':nth-child(6) > a').click()
      cy.get('#status').select('Conserto finalizado')
      cy.get('.update').click()

      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('#reopen > p').invoke('text').should('have.string', 'Reabrir solicitação')
      cy.get('#reopen > p').click()
      cy.get('.actions > [type="submit"]').click()
      cy.get('.EM_ANALISE').invoke('text').should('have.string', 'EM ANÁLISE')
    })

    it('Trying to reopen over 30 days', () => {

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
      cy.visit('/')
      cy.ClientLogout()
      cy.CreateAdmin()

      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
      cy.get('.content > form > button').click()
      cy.get('.content > form > button').click()
      
      cy.get('.budgetContainer > input').type('90')
      cy.get('.content > form > button').click()
      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('.waitingForm > form > button').click()
      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.works > button').click()

      cy.get('#detailed_problem_description').type('Muito pelo de gato dentro do motor está interferindo na ventilação interna')
      cy.get('#necessary_parts').type('Nenhuma, apenas limpeza')
      cy.get('.works > button').click()

      cy.get(':nth-child(6) > a').click()
      cy.get('#status').select('Conserto finalizado')
      cy.get('.update').click()

      cy.DefineClosedAtDate()

      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('#reopen > p').click()
      cy.get('.actions > [type="submit"]').click()
      cy.get('.toast').invoke('text').should('have.string', 'Essa solicitação não pode ser reaberta')
    })

    it('Reopening again', () => {
      
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
      cy.visit('/')
      cy.ClientLogout()
      cy.CreateAdmin()

      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      // cy.get('#status').select('Aguardando orçamento')
      cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
      cy.get('.content > form > button').click()
      cy.get('.content > form > button').click()
      
      cy.get('.budgetContainer > input').type('90')
      cy.get('.content > form > button').click()
      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('.waitingForm > form > button').click()
      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.works > button').click()

      cy.get('#detailed_problem_description').type('Muito pelo de gato dentro do motor está interferindo na ventilação interna')
      cy.get('#necessary_parts').type('Nenhuma, apenas limpeza')
      cy.get('.works > button').click()

      cy.get(':nth-child(6) > a').click()
      cy.get('#status').select('Conserto finalizado')
      cy.get('.update').click()

      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('#reopen > p').click()
      cy.get('.actions > [type="submit"]').click()

      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()

      // cy.get('#status').select('Aguardando orçamento')
      // cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
      // cy.get('.content > form > button').click()

      // cy.get('.budgetWatingConfirmation > input').clear()
      // cy.get('.budgetWatingConfirmation > input').type('0')
      cy.get('.content > form > button').click()
      
      // cy.get('.budgetContainer > input').clear()
      // cy.get('.budgetContainer > input').type('0')
      cy.get('.content > form > button').click()

      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('.waitingForm > form > button').click()
      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.works > button').click()

      cy.get('#detailed_problem_description').type('Muito pelo de gato dentro do motor está interferindo na ventilação interna')
      cy.get('#necessary_parts').type('Nenhuma, apenas limpeza')
      cy.get('.works > button').click()

      cy.get(':nth-child(6) > a').click()
      cy.get('#status').select('Conserto finalizado')
      cy.get('.update').click()

      cy.Logout()

      cy.GoToClient()
      cy.get('.view > button').click()
      cy.get('#reopen > p').should('not.exist')
      // cy.get('#reopen > p').click()
      // cy.get('.actions > [type="submit"]').click()

    })
})