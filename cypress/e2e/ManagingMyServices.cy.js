describe('HomePage', () => {
  it('Atribuição com sucesso', () => {
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
    cy.CreateEmployee("Paulo", "paulo@paulo.com")
    cy.get('.logout > button').click()
    cy.GoToEmployee("paulo@paulo.com")
    cy.get(':nth-child(1) > a').click()
    cy.get(':nth-child(6) > a').click()
    cy.get('#status').select('Aguardando orçamento')
    cy.get('.content > form > button').click()
    cy.get('.budgetContainer > input').type("200")
    cy.get('.content > form > button').click()
    cy.get('.logout > button').click()
    cy.GoToClient()
    cy.get('.view > button').click()
    cy.get('.yes > label').click()
    cy.get('.waitingForm > form > button').click()
    cy.ClientLogout()
    cy.GoToEmployee("paulo@paulo.com", false)
    cy.CreateOrder()
    cy.get(':nth-child(6) > a').click()
    cy.get('.assume').click()

    cy.get('ul > :nth-child(2) > a').click()
    cy.get('tbody > tr:first-child > :nth-child(5)').invoke('text').should("have.string", 'Paulo')
   })
})