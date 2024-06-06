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
      cy.get('#status').select('Aguardando orçamento')
      cy.get('.content > form > button').click()
      
      // cy.get('#status').select('Aguardando confirmação')
      cy.get('.budgetContainer > input').type('90')
      cy.get('.content > form > button').click()
      cy.Logout()

      cy.GoToClient()
      cy.get(':nth-child(4) > a').click()
      cy.get('.waitingForm > form > button').click()
      cy.Logout()

      cy.ChangeToAdmin()
      cy.get('ul > :nth-child(1)').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.works > button').click()
      // cy.get(':nth-child(6) > a').click()
  })
})