select *
From PortfolioProject..CovidDeaths
where continent is not null
order by 3,4

--select *
--From PortfolioProject..CovidVaccination
--order by 3,4

--select data we are going to be using

select location,date,total_cases,new_cases,total_deaths,population
From PortfolioProject..CovidDeaths
order by 1,2

--Looking at Total Cases vs Total Deaths

select location, date, total_cases,(cast(total_deaths as int),(total_deaths/total_cases)*100 as DeathPercentage
From PortfolioProject..CovidDeaths
where location like '%states%'
order by 1,2

--Looking at Total Cases Vs Population

select location, date, total_cases,population,(total_cases/population)*100 as PercentagePopulationInfected
From PortfolioProject..CovidDeaths
--where location like '%states%'
order by 1,2

--Looking at countries with Highest infection rate compared to population

select location, population, MAX(total_cases) as Highestinfectioncount,MAX(total_cases/population)*100 as PercentagePopulationInfected
From PortfolioProject..CovidDeaths
--where location like '%states%'
where continent is not null
Group by location,population
order by PercentagePopulationInfected desc

--Showing countries with highest death count per population

select location, MAX(cast(total_deaths as int)) as TotalDeathcount
From PortfolioProject..CovidDeaths
--where location like '%states%'
where continent is not null
Group by location
order by TotalDeathcount desc



--Lets break things by Continent

select continent, MAX(cast(total_deaths as int)) as TotalDeathcount
From PortfolioProject..CovidDeaths
--where location like '%states%'
where continent is not null
Group by continent
order by TotalDeathcount desc

--Global Numbers

select SUM(new_cases) as TotalCases,SUM(cast(new_deaths as int)) as TotalDeaths,SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From PortfolioProject..CovidDeaths
--where location like '%states%'
where continent is not null
--Group by date
order by 1,2 

--Looking at Total Population Vs Vaccination

select dea.continent, dea.location, dea.date ,dea.population , vac.new_vaccinations , SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location,dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
     on dea.location = vac.location   
	 and dea.date = vac.date
where dea.continent is not null
order by 2,3

--USE CTE

With PopvsVac (Continent,location, date, population,new_vaccinations,RollingPeopleVaccinated)
as
(
select dea.continent, dea.location, dea.date ,dea.population , vac.new_vaccinations , SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location,dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
     on dea.location = vac.location   
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3
)
select* ,(RollingPeopleVaccinated/Population)*100
From PopvsVac





--Temp Table

DROP table if exists #PercentPopulationVaccinated
create table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric,
)

Insert into #PercentPopulationVaccinated
select dea.continent, dea.location, dea.date ,dea.population , vac.new_vaccinations , SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location,dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
     on dea.location = vac.location   
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3

select* ,(RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated

--Creating view to store data for later visualization

Create view PercentPopulationVaccinated as
select dea.continent, dea.location, dea.date ,dea.population , vac.new_vaccinations , SUM(CONVERT(int,vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location,dea.Date) as RollingPeopleVaccinated
From PortfolioProject..CovidDeaths dea
Join PortfolioProject..CovidVaccinations vac
     on dea.location = vac.location   
	 and dea.date = vac.date
where dea.continent is not null
--order by 2,3
