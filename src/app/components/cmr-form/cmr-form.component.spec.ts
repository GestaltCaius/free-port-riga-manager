import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CmrFormComponent } from './cmr-form.component';

describe('CmrFormComponent', () => {
  let component: CmrFormComponent;
  let fixture: ComponentFixture<CmrFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CmrFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CmrFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
