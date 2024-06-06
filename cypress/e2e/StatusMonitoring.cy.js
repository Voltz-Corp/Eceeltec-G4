describe('test suite status monitoring', () => {
    it('Alterar o status de “Em análise” para “Agendado”', () => {
        cy.exec('python manage.py migrate');
        cy.DeleteAndCreateAdm();
        cy.visit('/');
        cy.on('uncaught:exception', (e, runnable) => {
            console.log('error', e);
            console.log('runnable', runnable);
            console.log('error', e.message);
            return false;
        });
        cy.CreateClient()
        cy.CreateSolicitation();
        cy.visit('/');
        cy.ClientLogout();
        cy.CreateAdmin();
        cy.get(':nth-child(1) > a').click();
        cy.get(':nth-child(6) > a').click();
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click();
        cy.get('.logout > button').click();
        cy.GoToClient();
        cy.get(':nth-child(4) > a').click();
        cy.get('.AGENDADO').invoke('text').should('have.string', 'AGENDADO')
    });
    it('Alterar o status de “Aceito” para “Em reparo”', () => {
        cy.exec('python manage.py migrate');
        cy.DeleteAndCreateAdm();
        cy.visit('/');
        cy.on('uncaught:exception', (e, runnable) => {
            console.log('error', e);
            console.log('runnable', runnable);
            console.log('error', e.message);
            return false;
        });
        cy.CreateClient()
        cy.CreateSolicitation();
        cy.visit('/');
        cy.ClientLogout();
        cy.CreateAdmin();
        cy.get(':nth-child(1) > a').click();
        cy.get(':nth-child(6) > a').click();
        cy.get('.scheduleDateContainer > input').invoke('removeAttr', 'type').type('2024-06-18')
        cy.get('.content > form > button').click();
        cy.get('#status').select('Aguardando orçamento')
        cy.get('.content > form > button').click()
        cy.get('.budgetContainer > input').type('50')
        cy.get('.content > form > button').click()
        cy.get('.logout > button').click();
        cy.GoToClient();
        cy.get(':nth-child(4) > a').click();
        cy.get('.waitingForm > form > button').click()
        cy.ClientLogout();
        cy.get('#employee > a').click()
        cy.get('#email').type('eceel-Tec@eceeltec.com')
        cy.get('#password').type('obGWjpaTayKJWpBiFSMm')
        cy.get('button').click()
        cy.get(':nth-child(1) > a').click();
        cy.get(':nth-child(6) > a').click();
        cy.get('#detailed_problem_description').type('Tá muito velho')
        cy.get('#necessary_parts').type('Todas')
        cy.get('.works > button').click();
        cy.ClientLogout();
        cy.GoToClient();
        cy.get('tbody > tr > :nth-child(1)').invoke('text').should('have.string', "EM REPARO")
    });
});