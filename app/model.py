from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List, Optional, Literal
from datetime import date
from enum import Enum

class EducationLevel(str, Enum):
    HIGH_SCHOOL = "high_school"
    ASSOCIATE = "associate"
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"
    DIPLOMA = "diploma"
    CERTIFICATE = "certificate"

class EmploymentType(str, Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    FREELANCE = "freelance"
    INTERNSHIP = "internship"
    TEMPORARY = "temporary"

class SkillLevel(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class ContactInformation(BaseModel):
    """Contact details of the candidate"""
    full_name: str = Field(..., description="Full name of the candidate")
    email: Optional[EmailStr] = Field(None, description="Primary email address")
    phone: Optional[str] = Field(None, description="Phone number with country code")
    location: Optional[str] = Field(None, description="City, State/Province, Country")
    linkedin: Optional[HttpUrl] = Field(None, description="LinkedIn profile URL")
    github: Optional[HttpUrl] = Field(None, description="GitHub profile URL")
    portfolio: Optional[HttpUrl] = Field(None, description="Personal website or portfolio")
    other_links: Optional[List[HttpUrl]] = Field(default_factory=list, description="Other relevant links")


class Education(BaseModel):
    """Educational background entry"""
    institution: str = Field(..., description="Name of educational institution")
    degree: str = Field(..., description="Degree or certification name")
    level: Optional[EducationLevel] = Field(None, description="Level of education")
    start_date: Optional[date] = Field(None, description="Start date")
    end_date: Optional[date] = Field(None, description="End date or expected graduation")
    gpa: Optional[float] = Field(None, ge=0.0, le=4.0, description="GPA on 4.0 scale")
    location: Optional[str] = Field(None, description="Location of institution")
    

class WorkExperience(BaseModel):
    """Professional work experience entry"""
    company: str = Field(..., description="Company or organization name")
    position: str = Field(..., description="Job title or position")
    employment_type: Optional[EmploymentType] = Field(None, description="Type of employment")
    start_date: Optional[date] = Field(None, description="Start date")
    end_date: Optional[date] = Field(None, description="End date (None if current)")
    is_current: bool = Field(default=False, description="Currently working here")
    location: Optional[str] = Field(None, description="Job location")
    description: Optional[str] = Field(None, description="Brief role description")
    responsibilities: List[str] = Field(default_factory=list, description="Key responsibilities and achievements")
    technologies: List[str] = Field(default_factory=list, description="Technologies/tools used")
    duration_years: Optional[float] = Field(None, description="Duration in years (can be fractional)")


class Skill(BaseModel):
    """Individual skill entry"""
    name: str = Field(..., description="Skill name")
    category: Optional[str] = Field(None, description="Category (e.g., Programming, Design, Management)")
    level: Optional[SkillLevel] = Field(None, description="Proficiency level")
    

class Certification(BaseModel):
    """Professional certification or license"""
    name: str = Field(..., description="Certification name")
    issuing_organization: str = Field(..., description="Organization that issued certification")
    issue_date: Optional[date] = Field(None, description="Date obtained")

class Project(BaseModel):
    """Personal or professional project"""
    name: str = Field(..., description="Project name")
    description: str = Field(..., description="Project description")
    role: Optional[str] = Field(None, description="Your role in the project")
    technologies: List[str] = Field(default_factory=list, description="Technologies used")
    url: Optional[HttpUrl] = Field(None, description="Project URL or demo link")

class Language(BaseModel):
    """Language proficiency"""
    language: str = Field(..., description="Language name")
    proficiency: Literal["native", "fluent", "professional", "intermediate", "basic"] = Field(
        ..., description="Proficiency level"
    )

class VolunteerExperience(BaseModel):
    """Volunteer work or community service"""
    organization: str = Field(..., description="Organization name")
    role: str = Field(..., description="Volunteer role or position")
    start_date: Optional[date] = Field(None, description="Start date")
    end_date: Optional[date] = Field(None, description="End date")
    description: Optional[str] = Field(None, description="Description of work")
 
class CVAnalysis(BaseModel):
    """Metadata and analysis of the CV"""
    total_years_experience: Optional[float] = Field(None, description="Calculated total years of work experience")
    career_level: Optional[Literal["entry", "junior", "mid", "senior", "lead", "executive"]] = Field(
        None, description="Assessed career level"
    )
    primary_industry: Optional[str] = Field(None, description="Primary industry or domain")
    job_titles: List[str] = Field(default_factory=list, description="All job titles held")
    companies_worked_at: List[str] = Field(default_factory=list, description="All companies worked at")
    education_summary: Optional[str] = Field(None, description="Highest education level")
    has_gaps: bool = Field(default=False, description="Employment gaps detected")
    gap_details: Optional[List[str]] = Field(default_factory=list, description="Details about employment gaps")
    job_hopping_score: Optional[float] = Field(None, ge=0, le=10, description="Job stability score (0-10)")
    keyword_density: Optional[dict] = Field(default_factory=dict, description="Important keywords and frequency")

class AgentAssessment(BaseModel):
    """Intelligent AI-driven assessment and recommendations for candidate evaluation."""

    overall_rating: Literal["excellent", "strong", "good", "average", "below_average", "poor"] = Field(
        ...,
        description=(
            "Overall qualitative evaluation of the candidate based on full CV analysis. "
            "Reflects how well the candidate aligns with expected role requirements, considering "
            "skills, experience, achievements, and consistency."
        ),
    )

    rating_score: float = Field(
        ...,
        ge=0,
        le=100,
        description=(
            "Numerical rating (0–100) representing the candidate's overall fit and quality. "
            "Derived from experience, technical skill depth, and career trajectory."
        ),
    )

    strengths: List[str] = Field(
        default_factory=list,
        description=(
            "Key strengths or differentiators identified from the CV. "
            "May include notable achievements, advanced technical expertise, leadership, or domain specialization."
        ),
    )

    weaknesses: List[str] = Field(
        default_factory=list,
        description=(
            "Areas of concern or opportunities for improvement, such as limited exposure to certain technologies, "
            "short tenure in roles, or lack of recent upskilling."
        ),
    )

    red_flags: List[str] = Field(
        default_factory=list,
        description=(
            "Critical issues or warning signals that may impact hiring decision. "
            "Examples: frequent job changes, long employment gaps, inconsistent career progression, or unverifiable claims."
        ),
    )

    suitable_roles: List[str] = Field(
        default_factory=list,
        description=(
            "List of job titles or role types for which this candidate would be a strong match, "
            "based on their demonstrated experience, skills, and achievements."
        ),
    )

    experience_assessment: str = Field(
        ...,
        description=(
            "Narrative assessment of the candidate's professional experience and career trajectory. "
            "Summarizes progression, leadership exposure, and depth of domain experience."
        ),
    )

    technical_assessment: str = Field(
        ...,
        description=(
            "Detailed evaluation of the candidate's technical competencies, tool familiarity, "
            "and current relevance of their skill set. Includes depth and breadth of technical expertise."
        ),
    )

    cultural_fit_indicators: List[str] = Field(
        default_factory=list,
        description=(
            "Indicators suggesting cultural or organizational fit, derived from volunteer work, interests, "
            "communication tone, or teamwork experience mentioned in the CV."
        ),
    )

    recommended_next_steps: List[str] = Field(
        default_factory=list,
        description=(
            "Concrete HR actions recommended by the agent, such as 'Invite for technical screening', "
            "'Schedule cultural interview', 'Check references', or 'Reject with feedback'."
        ),
    )

    summary: str = Field(
        ...,
        description=(
            "A concise 2–3 sentence executive summary of the candidate’s overall profile, "
            "highlighting their main strengths, potential fit, and hiring recommendation."
        ),
    )

    interview_focus_areas: List[str] = Field(
        default_factory=list,
        description=(
            "Specific topics or areas to explore further during interviews. "
            "Examples: 'Team leadership experience', 'System design depth', 'Handling of large-scale data pipelines'."
        ),
    )

class CandidateCV(BaseModel):
    """Complete structured CV/Resume data"""
    
    # Core Information
    contact_information: ContactInformation
    
    # Professional Summary
    summary: Optional[str] = Field(None, description="Professional summary or objective")
    
    # Experience & Education
    work_experience: List[WorkExperience] = Field(default_factory=list, description="Work history")
    education: List[Education] = Field(default_factory=list, description="Educational background")
    
    # Skills
    skills: List[Skill] = Field(default_factory=list, description="All skills")
    
    # Additional Sections
    certifications: List[Certification] = Field(default_factory=list, description="Certifications and licenses")
    projects: List[Project] = Field(default_factory=list, description="Notable projects")
    languages: List[Language] = Field(default_factory=list, description="Language proficiencies")
    volunteer_experience: List[VolunteerExperience] = Field(default_factory=list, description="Volunteer work")
    
    # Additional Information
    interests: Optional[List[str]] = Field(default_factory=list, description="Personal interests or hobbies")
    references: Optional[str] = Field(None, description="References note (usually 'Available upon request')")
    
    # Analysis
    cv_analysis: Optional[CVAnalysis] = Field(None, description="Automated CV analysis")
    
    # Agent Intelligence Assessment
    agent_assessment: Optional[AgentAssessment] = Field(
        None, 
        description="Intelligent agent analysis, recommendations, and hiring decision support"
    )
    
    # Metadata
    source_file: Optional[str] = Field(None, description="Original file name")


#------------------------------------------------------------

from pydantic import BaseModel, Field
from typing import List, Literal


class ScoreBreakdown(BaseModel):
    """Detailed breakdown of match scoring"""
    skills_score: float = Field(..., ge=0, le=40, description="Points from skills match (max 40)")
    experience_score: float = Field(..., ge=0, le=30, description="Points from experience match (max 30)")
    education_score: float = Field(..., ge=0, le=20, description="Points from education match (max 20)")
    career_level_score: float = Field(..., ge=0, le=10, description="Points from career level fit (max 10)")


class JobMatchResult(BaseModel):
    """Result of matching a candidate CV against a job description"""
    
    # Basic Information
    candidate_name: str = Field(..., description="Full name of the candidate")
    job_title: str = Field(..., description="Job title being matched against")
    
    # Overall Score
    overall_score: float = Field(..., ge=0, le=100, description="Total match score out of 100")
    
    # Score Breakdown
    breakdown: ScoreBreakdown = Field(..., description="Detailed scoring breakdown by category")
    
    # Skills Analysis
    skills_matched: List[str] = Field(default_factory=list, description="Required skills the candidate has")
    skills_missing: List[str] = Field(default_factory=list, description="Required skills the candidate lacks")
    skills_match_percentage: float = Field(..., ge=0, le=100, description="Percentage of required skills matched")
    
    # Experience Analysis
    candidate_experience_years: float = Field(..., ge=0, description="Candidate's total years of experience")
    required_experience_years: float = Field(..., ge=0, description="Required years of experience for job")
    experience_gap: str = Field(..., description="Description of experience gap or fit")
    
    # Education & Career Level
    education_match: bool = Field(..., description="Whether education requirements are met")
    career_level_match: Literal["exact_match", "one_level_off", "two_plus_levels_off"] = Field(
        ..., description="How well candidate's career level matches job"
    )
    
    # Recommendation
    recommendation: str = Field(
        ..., 
        min_length=10,
        description="Brief 2-3 sentence recommendation summary"
    )
    
    # Match Category (for classification)
    match_category: Literal["strong_match", "moderate_match", "weak_match"] = Field(
        ..., description="Overall match category: strong (≥80), moderate (60-79), weak (<60)"
    )