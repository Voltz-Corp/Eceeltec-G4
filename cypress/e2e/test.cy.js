
describe('home page', () => {
  it('passes', () => {
    

    cy.visit('/');

    //menuHamburger not defined!?
    cy.on("uncaught:exception", (e, runnable) => {
      console.log("error", e);
      console.log("runnable", runnable);
      console.log("error", e.message);
      return false;
      });

    
    cy.get('#employee > a').click()

    // cy.get('#email').type('admin')
    // cy.get('#password').type('admin')
    // cy.get('button').click()

  })
})
