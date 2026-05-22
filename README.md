# 🏢 Django ERP System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![React](https://img.shields.io/badge/React-18-cyan)
![License](https://img.shields.io/badge/License-MIT-yellow)

A full-featured **Enterprise Resource Planning (ERP)** system built with Django REST Framework backend and React frontend. Designed for small to mid-size businesses needing integrated operations management.

## 📦 Modules

| Module | Features |
|--------|---------|
| 👥 **HR** | Employees, departments, payroll, attendance, leave management |
| 📦 **Inventory** | Products, stock levels, purchase orders, suppliers, warehouses |
| 💰 **Finance** | Accounts, invoicing, expenses, profit & loss, balance sheet |
| 🤝 **CRM** | Leads, clients, deals, follow-ups, sales pipeline |
| 📋 **Projects** | Tasks, milestones, time tracking, team assignment |
| 📊 **Reports** | Custom reports, PDF/Excel export, dashboard analytics |

## 🏗️ Architecture

```
React Frontend (SPA)
        ↓
Django REST Framework API
        ↓
PostgreSQL Database
        ↓
Celery + Redis (async tasks)
        ↓
PDF/Excel Report Generation
```

## ✨ Features

- 🔐 Role-based access control (Admin, Manager, Staff)
- 📱 Responsive dashboard with charts
- 📄 PDF & Excel report export
- 🔔 Real-time notifications
- 🌍 Multi-currency support
- 🏭 Multi-branch / multi-warehouse support
- ⚙️ REST API with Swagger docs

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 + DRF |
| Frontend | React 18 + Tailwind CSS |
| Database | PostgreSQL 15 |
| Cache | Redis |
| Task Queue | Celery |
| Auth | JWT (SimpleJWT) |
| Reports | ReportLab + openpyxl |

## 🚀 Quick Start

```bash
git clone https://github.com/rashedkhanrubel-spec/django-erp-system
cd django-erp-system

# Backend
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend
cd frontend
npm install
npm run dev
```

## 📁 Project Structure

```
django-erp-system/
├── apps/
│   ├── hr/              # HR & payroll module
│   ├── inventory/       # Stock & warehouse module
│   ├── finance/         # Accounting module
│   ├── crm/             # Client management module
│   └── reports/         # Reporting engine
├── frontend/            # React SPA
├── config/              # Django settings
├── manage.py
└── requirements.txt
```

## 📬 Contact

Built by [Md Rashed Khan](https://www.freelancer.com/u/rashedkhanrubel) — Available for ERP & business application projects.

