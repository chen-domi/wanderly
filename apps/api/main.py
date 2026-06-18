from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Wanderly API",
    version="0.1.0",
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root() -> dict[str, str]:
    return {"name": "Wanderly API", "status": "running"}

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/trips/plan")
def plan_trip(payload: dict) -> dict:
    return {
        "trip_brief": {
            "intent": payload,
            "mode": "mock",
            "status": "planned",
        },
        "packages": [
            {
                "label": "Best Overall",
                "summary": "Balanced package with reasonable cost and convenience.",
                "estimated_total": 2450,
            },
            {
                "label": "Most Effortless",
                "summary": "Better flights, closer lodging, and smoother logistics.",
                "estimated_total": 3800,
            },
            {
                "label": "Leanest Viable",
                "summary": "Lower cost with acceptable tradeoffs.",
                "estimated_total": 1750,
            },
        ],
    }
