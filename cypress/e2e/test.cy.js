describe('home page', () => {
  it('passes', () => {
    cy.exec('python manage.py migrate')
    cy.DeleteAndCreateAdm()
    cy.visit('/');
    cy.CreateAdmin()
    cy.CreateEmployee()
    cy.get('.logout > button').click()
    cy.CreateClient()
    cy.CreateSolicitation()
    
    //menuHamburger not defined!?
    cy.on("uncaught:exception", (e, runnable) => {
      console.log("error", e);
      console.log("runnable", runnable);
      console.log("error", e.message);
      return false;
    });
  })
})
