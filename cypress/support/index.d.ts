/// <reference types="cypress" />

declare namespace Cypress {
  interface Chainable<Subject> {
    DeleteAndCreateAdm(): Chainable<any>;
    CreateClient(name?: string, email?: string): Chainable<any>;
    CreateClient(name?: string, email?: string): Chainable<any>;
    CreateOrder(): Chainable<any>;
    CreateEmployee(name?: string, email?: string): Chainable<any>;
    CreateSolicitation(): Chainable<any>;
    ClientLogout(): Chainable<any>;
    GoToClient(email: string, password: string): Chainable<any>;
    CreateAdmin(): Chainable<any>;
    ChangeToAdmin(): Chainable<any>;
    GoToEmployee(email: string, firstLogin: boolean): Chainable<any>;
    Logout(): Chainable<any>;
  }
}
