import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { VehiculoService } from '../services/vehiculo';


@Component({
  selector: 'app-vehiculos',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './vehiculos.html',
  styleUrls: ['./vehiculos.css'],



})
export class Vehiculos implements OnInit {
  vehiculoForm!: FormGroup;
  vehiculos: any[] = [];
  errorMessage: string = '';

  constructor(private fb: FormBuilder, private vehiculoService: VehiculoService) {}

  ngOnInit(): void {
    this.vehiculoForm = this.fb.group({
      placa: ['', [Validators.required, Validators.pattern(/^.{3}-.+/)]],
      propietario: ['', Validators.required],
      marca: ['', Validators.required],
      fabricacion: [
        '',
        [
          Validators.required,
          Validators.min(1900),
          Validators.max(new Date().getFullYear()),
        ],
      ],
      valor_comercial: ['', [Validators.required, Validators.min(0)]],
    });

    this.cargarVehiculos();
  }

  registrarVehiculo(): void {
    if (this.vehiculoForm.invalid) return;

    this.vehiculoService.crearVehiculo(this.vehiculoForm.value).subscribe({
      next: (res) => {
        this.vehiculos.push(res);
        this.vehiculoForm.reset();
        this.errorMessage = '';
      },
      error: (err) => {
        this.errorMessage = err.error?.detail || 'Error al registrar vehículo';
      },
    });
  }

  cargarVehiculos(): void {
    this.vehiculoService.listarVehiculos().subscribe({
      next: (res) => (this.vehiculos = res),
      error: (err) => console.error(err),
    });
  }

  esAltoImpuesto(vehiculo: any): boolean {
    return vehiculo.impuesto > 500;
  }
}
