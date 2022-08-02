import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DateTimeService {
  date:any;

  constructor() { 
    this.date = new DateTimeService();
  }

  getDate()
  {
    return this.date;
  }
}
