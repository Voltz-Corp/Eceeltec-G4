function formatDate(date) {
  const month = date.getMonth() + 1;
  const formattedMonth = month < 10 ? `0${month}` : `${month}`;

  const day = date.getDate();
  const formattedDay = day < 10 ? `0${day}` : `${day}`;

  return `${date.getFullYear()}-${formattedMonth}-${formattedDay}`
}

const today = new Date()
const todayFormatted = formatDate(today)
const oneMonthFromToday = formatDate(new Date(today.getFullYear(), today.getMonth() + 1, today.getDate()))

  describe('home page', () => {
    it('Definindo data com sucesso', () => {
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
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click()
        cy.GoToClient()
        cy.get('tbody > tr > :nth-child(3)').invoke('text').should('have.string', "18 de Junho de 2024")
        cy.get('.AGENDADO').invoke('text').should('have.string', 'AGENDADO')

     })

    it('Definindo orçamento com sucesso', () => {
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
        cy.get(':nth-child(1) > a').click()
        cy.get(':nth-child(6) > a').click()
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click()
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('50')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click()
        cy.GoToClient()
        cy.get(':nth-child(4) > a').click()
        cy.get('.price > span').invoke('text').should('have.string', "50,00")
        cy.get('.waitingForm > p').invoke('text').should('have.string', "Você deseja prosseguir com o serviço?")
     })
  
    it('inserindo data inválida', () => {


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
      cy.get(':nth-child(1) > a').click()
      cy.get(':nth-child(6) > a').click()
      cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2020-01-12')
      cy.get('.content > form > button').click()
      cy.get('span').invoke('text').then((text) => {
        const formattedText = text.trim();
        expect(formattedText).to.contain(`A data precisa estar entre ${todayFormatted} e ${oneMonthFromToday}!`);
      });
  })
})
