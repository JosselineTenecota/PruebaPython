import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Vehiculos } from "./vehiculos/vehiculos";


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Vehiculos],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend-vehicul');
}
