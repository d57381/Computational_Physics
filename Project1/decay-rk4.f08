program decay
  real :: pu(200), an(200), t(200)
  real, parameter :: tau = 126.58
  real :: tt = 5.0*tau
  real :: pu0 = 100.
  integer :: ns
  integer :: nt
  real :: dt
  real :: y(200)
  open(7, file = "results")
  print*, "Enter the time step size "
  read*, ns
  nt = 200/ns
  dt = tt*ns/200.
  pu(1)=pu0
  t(1) = 0.0
  
100 format(3(2x, e12.5))
  do i=1, nt-1
     t(i+1) = t(i)+dt
     an(i+1) = 100*exp(-t(i+1)/tau)
!     pu(i+1) = pu(i)*(1-dt/tau)
!     write(7,100), t(i+1), an(i+1), pu(i+1)
  enddo
  call rk4(100.0, dt, y, 200)
  do i=1, nt-1
     write(7,100) t(i+1), y(i+1), an(i+1)
  enddo
  close(7)
end program decay

subroutine rk4(y0, dt, y, n)
  external fyt
  real :: y(n), fyt
  y(1) = y0
  do i=1, n-1
     y105 = y(i)+0.5*dt*fyt(y(i))
     y205= y(i)+0.5*fyt(y105)*dt
     y11 = y(i)+dt*fyt(y205)
     y(i+1) = y(i)+1/6.0*dt*(fyt(y(i))+2*fyt(y105)+2*fyt(y205)+fyt(y11))
  enddo
  return
end subroutine rk4

function fyt(y)
  real :: y
  fyt = -y/126.58
return
end function fyt
