import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from '../src/app/app';
import { provideRouter } from '@angular/router';
import { routes } from '../src/app/app.routes';
import { importProvidersFrom } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    importProvidersFrom(HttpClientModule)
  ]
});