# A structured dictionary designed for business, financial, or operational summary metrics
summary_metrics = {
    "metadata": {
        "report_name": "Q3 Performance Summary",
        "generated_at": "2026-09-19T10:47:00Z",
        "currency": "USD",
        "time_frame": "Q3 2026"
    },
    "key_performance_indicators": {
        "total_revenue": {
            "value": 1250500.00,
            "target": 1200000.00,
            "status": "exceeded",
            "yoy_growth_percentage": 14.2
        },
        "net_profit_margin": {
            "value": 22.4,
            "target": 20.0,
            "status": "on_track",
            "yoy_growth_percentage": 2.1
        },
        "customer_acquisition_cost": {
            "value": 45.50,
            "target": 50.00,
            "status": "on_track",
            "yoy_growth_percentage": -8.3  # Negative is positive for costs
        }
    },
    "operational_metrics": {
        "active_users": {
            "current": 45200,
            "previous_period": 41100,
            "change_percentage": 9.9
        },
        "churn_rate": {
            "current": 2.1,
            "previous_period": 2.5,
            "change_percentage": -16.0
        }
    },
    "system_health": {
        "uptime_percentage": 99.98,
        "average_response_time_ms": 142
    }
}

# Printing the structured dictionary cleanly
import json
print(json.dumps(summary_metrics, indent=4))
