describe('Service rating', () => {
    it('avaliação com sucesso', () => {
      cy.exec('python manage.py migrate')
      cy.DeleteAndCreateAdm()
      cy.visit('/')
      cy.on("uncaught:exception", (e, runnable) => {
          console.log("error", e);
          console.log("runnable", runnable);
          console.log("error", e.message);
          return false;
          });
  
      cy.CreateClient("Sophia Gallindo")
      cy.CreateSolicitation()
      cy.visit('/')
      cy.ClientLogout()
      cy.CreateAdmin()
      cy.CreateEmployee()
      cy.CreateEmployee("Paulo", "paulo@paulo.com")
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
      cy.get('#status').select('Conserto finalizado')
      cy.get('.update').click()
      cy.get('.logout > button').click()
      cy.GoToClient()
      cy.get(':nth-child(4) > a').click()
      cy.get('#rate > p').click()
      cy.get('.ratingAttendance > :nth-child(5)').click()
      cy.get('.ratingService > :nth-child(5)').click()
      cy.get('.ratingTime > :nth-child(5)').click()
      cy.get('#notes').type("Serviço excelente, produto entregue no tempo estimado e atendimento de ótima qualidade")
      cy.get('.rating-submit').click()
    })
  })
  