import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VehiculoService {
  private apiUrl = 'http://localhost:8000/api/vehiculos';

  constructor(private http: HttpClient) {}

  listarVehiculos(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  crearVehiculo(vehiculo: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, vehiculo);
  }
}
