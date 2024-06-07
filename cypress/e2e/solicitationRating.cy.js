describe('Service rating', () => {
    it('Avaliação com sucesso', () => {
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
      cy.get('.view > button').click()
      cy.get('#rate > p').click()

      cy.get('.ratingAttendance > :nth-child(5)').should("have.class", "active")
      cy.get('.ratingService > :nth-child(5)').should("have.class", "active")
      cy.get('.ratingTime > :nth-child(5)').should("have.class", "active")
      cy.get('#notes').should("have.value", 'Serviço excelente, produto entregue no tempo estimado e atendimento de ótima qualidade')
    })

    it('Excedendo o limite de caracteres em comentário.', () => {
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
      cy.get('#notes').type(`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`)
      cy.get('.rating-submit').click()
      cy.get('.error-message').invoke("text").then((text) => {
        const formattedText = text.trim();
        expect(formattedText).to.contain(`O seu comentário não pode ultrapassar 200 caracteres!`);
      })
    })
  })
  