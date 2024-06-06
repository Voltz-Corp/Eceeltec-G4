describe('HomePage', () => {
  it('Designar um técnico com sucesso', () => {
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
      cy.CreateEmployee()
      cy.get('#sidebarNav > ul > :nth-child(1)').click()
      cy.CreateOrder()
      cy.get(':nth-child(6) > a').click()
      cy.get('#tecnician').select("Robson")
      cy.get('.update').click()
      cy.get('.employee').invoke('text').should("have.string", "Robson")
   })

//    it('Remover uma ordem de serviço com sucesso', () => {
//     cy.exec('python manage.py migrate')
//     cy.DeleteAndCreateAdm()
//     cy.visit('/')
//     cy.on("uncaught:exception", (e, runnable) => {
//         console.log("error", e);
//         console.log("runnable", runnable);
//         console.log("error", e.message);
//         return false;
//         });

//     cy.CreateSolicitation("Sophia Gallindo")
//     cy.visit('/')
//     cy.ClientLogout()
//     cy.CreateAdmin()
//     cy.get(':nth-child(1) > a').click()
//     cy.get(':nth-child(6) > a').click()
//     cy.get('#status').select('Aguardando orçamento')
//     cy.get('.content > form > button').click()
//     cy.get('.budgetContainer > input').type("200")
//     cy.get('.content > form > button').click()
//     cy.get('.logout > button').click()
//     cy.GoToClient()
//     cy.get(':nth-child(4) > a').click()
//     cy.get('.yes > label').click()
//     cy.get('.waitingForm > form > button').click()
//     cy.ClientLogout()
//     cy.ChangeToAdmin()
//     cy.get('ul > :nth-child(1) > a').click()
//     cy.CreateOrder()
//     cy.get(':nth-child(6) > a').click()
//     cy.get('#status').select('Cancelado')
//     cy.get('.update').click()
//     cy.get('ul > :nth-child(1) > a').click()
//     cy.get('.deleteOrderRequest').click()
//     cy.get('.deleteRequestOrder').click()
//     cy.get('tbody > tr:first-child').should("not.exist")
//  })
})